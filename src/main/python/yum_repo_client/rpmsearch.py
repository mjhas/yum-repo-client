from yum_repo_client.rpmfile import RpmFile
import rpm
import re

class RpmSearch():
  def search_rpms_with_name(self, rpm_name, files, sort_desc = False):
    matcher = re.compile(rpm_name)
    found_rpms = [RpmFile(rpm_file['filename']) for rpm_file in files if matcher.search(rpm_file['filename'])]

    return self._sort_rpms(found_rpms, sort_desc)

  def _sort_rpms(self, rpm_list, sort_desc):
    rg = {}
    
    for rpm_file in rpm_list:
      if rg.has_key(rpm_file.name):
        rg.get(rpm_file.name).append(rpm_file)
      else:
        rg[rpm_file.name] = [rpm_file]
    
    keys = rg.keys()
    for key in keys:
      rg.get(key).sort(cmp=self._compare_rpms_by_version, reverse=sort_desc)
      
    keys.sort(reverse=sort_desc)
    
    sorted_list = []
    for key in keys:
      sorted_list.extend(rg.get(key))
    
    #rpm_list.sort(cmp=self._compare_rpms_by_version, reverse=sort_desc)
    
    return sorted_list
    

  def _compare_rpms_by_version(self, rpm_file1, rpm_file2):
    if rpm_file1.name != rpm_file2.name:
      return rpm_file1.name < rpm_file2.name
    return rpm.labelCompare(('1', rpm_file1.version, rpm_file1.release), ('1', rpm_file2.version, rpm_file2.release))
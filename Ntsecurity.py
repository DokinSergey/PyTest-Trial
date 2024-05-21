import win32security
import ntsecuritycon as ntcon
# as con

FileName = "C://exe//DEV22001"

print(FileName)

userx, domain, type = win32security.LookupAccountName ("", 'OMC170GE')
print(userx, domain)


sd = win32security.GetFileSecurity(FileName, win32security.DACL_SECURITY_INFORMATION)
dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()

# предпологаемые опции
# FILE_ADD_FILE | FILE_ADD_SUBDIRECTORY | FILE_DELETE_CHILD | FILE_TRAVERSE | FILE_GENERIC_READ | FILE_READ_ATTRIBUTES| con.FILE_ADD_SUBDIRECTORY

#dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
# dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, usery)

dacl.AddAccessAllowedAce(win32security.ACL_REVISION, ntcon.FILE_GENERIC_READ | ntcon.FILE_TRAVERSE | ntcon.FILE_READ_ATTRIBUTES | ntcon.FILE_APPEND_DATA, userx)

sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
win32security.SetFileSecurity(FileName, win32security.DACL_SECURITY_INFORMATION, sd)
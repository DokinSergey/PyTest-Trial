import os
from shutil import copy2,rmtree,make_archive,copytree
from time import sleep
from rich import print
from zipfile import ZipFile,ZIP_DEFLATED
import tempfile
#---------------------------------------------------------------------------
with tempfile.TemporaryDirectory() as tmpdirname:
        
    CurPath = os.path.realpath('')
    Ts1Path = os.path.join(os.path.dirname(CurPath),'TestDir1')
    Ts2Path = os.path.join(Ts1Path,'TestDir2')
    TstFile = os.path.join(CurPath,'Test_v8i.log.txt')
    NewFile = os.path.join(Ts2Path,'Test_v8i.log.txt')
    ZipFlNm = os.path.join(Ts2Path,'Test_v8i.zip')
    print(CurPath,Ts2Path)
    print(TstFile)
    print(NewFile)
    #---------------------------------------------------------------------------os.path.normpath(path)
    if not os.path.isdir(Ts2Path):
        os.makedirs(Ts2Path,exist_ok=True)
    # copy2(TstFile,NewFile)
    copytree(CurPath,tmpdirname,dirs_exist_ok=True)
    print(root_dir := tmpdirname)
    print(base_name := os.path.join(Ts2Path, 'zip'))
    make_archive(base_name, 'zip', root_dir)
        # print(docArxPath := os.path.join(ArxPath,'Documents'))
        # with tempfile.TemporaryDirectory() as tmpdirname: #docArxPath
    # print('created temporary directory', tmpdirname)
    # with ZipFile(ZipFlNm, "w",compression=ZIP_DEFLATED,compresslevel=9, allowZip64=True) as myzip:
        # myzip.write(TstFile, arcname=os.path.basename(TstFile))
    input(':-> ')
# rmtree(Ts1Path)
os._exit(0)
import os;
import shutil;

print "This program compares two folders and deletes files in the First folder \nwhich have the same name and size of a file in the Second Folder ";

path_1 = raw_input("Type the path of the First Folder (Files will be delated): ");
path_2 = raw_input("Type the path of the Second Folder: ");

#path_1 = "/media/felipe/DOCUMENTOS/ARCHIVOS_PARAORGANIZAR/TESIS_DOCTORADO/Ubuntu16/TESIS_Results";
#path_2 = "/media/felipe/DOCUMENTOS/ARCHIVOS_PARAORGANIZAR/TESIS_DOCTORADO/REFERENCE/TESIS_Results";

def Comparing(file_path1,path2,list_to_delete):
    list = os.listdir(path2);
    file_path1_name = file_path1.split("/");
    file1 = file_path1_name[-1];
#    print "file to compare ", file1;
    if(os.path.isfile(file_path1)):
#        print "IS A FILE";
        f1 = os.stat(file_path1);
        size_file1 = f1.st_size;
        # loop over the second path
        for files in list:
            file_path2 = path2+'/'+files;
            if(os.path.isfile(file_path2)):
                f2 = os.stat(file_path2);
                size_file2 = f2.st_size;
                if((os.path.isfile(file_path2)) and (file1 == files) and (size_file1 == size_file2)):
#                    print "First: ", file_path2;
#                    print "removed file: ", file_path1;
                    if(not(file_path1 in list_to_delete)):
                       list_to_delete.append(file_path1);
                    continue;
            if(os.path.isdir(file_path2)):
                Comparing(file_path1,file_path2,list_to_delete);
    return list_to_delete; 

def FirstLoop(path1,path2,list_del):
    list_1 = os.listdir(path1);
    for file1 in list_1:
        file_path1 = path1+'/'+file1;
        if(os.path.isfile(file_path1) and (not(file_path1 in list_del))):
            List_to_Delete.append(Comparing(file_path1,path2,list_del));
#            List_to_Delete.append(Comparing(file_path1,path2,list_del));
#            print List_to_Delete;
        if(os.path.isdir(file_path1)):
            FirstLoop(file_path1,path2,list_del);
    return List_to_Delete;
    
def DeletingFolders(path1,counter):
    list_1 = os.listdir(path1);
    for files in list_1:
        file_path = path1+'/'+files;
        if(os.path.isdir(file_path)):
            list_tmp = os.listdir(file_path);
            if(list_tmp == []):
                print "Folder ", files, " is empty";
                print "Removed folder: ", file_path;
                os.rmdir(file_path);
            else:
                counter = DeletingFolders(file_path,counter+1);
        if(os.path.isfile(file_path)):
            continue;
    return counter;

if(path_1 != path_2):
    empty_list = [];
    Full_list = [];
    List_to_Delete = [];

    Full_list = FirstLoop(path_1,path_2,empty_list);
    List_to_Delete = Full_list[-1];
#    print List_to_Delete;
    
    if(not(Full_list[-1] == [])):
        for i in List_to_Delete:
            print "removed file: ", i;
            os.remove(i);        
            #Deleting empty folders within a path
        c = 1;
        for i in range(1,DeletingFolders(path_1,c)):
            DeletingFolders(path_1,c);
    #Cleaning empty folders
    #    Cleaning(path_1);
    print "DONE"
else:
    print "BE CAREFULL!!!!!!! The TWO PATHS MUST BE DIFFERENT"

        

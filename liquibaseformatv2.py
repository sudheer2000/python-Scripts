f = open("/Users/i1097/Documents/2021_08_25_09_00_01_SD19172.sql", "w")
uid="1634807991"
with open('/Users/i1097/Documents/2021_08_25_09_00_01.sql') as file:
    i = 0
    for line in file:
        # reading each word
        if not line.strip().startswith("--"):
            if (not line.strip().startswith("GRANT")):
                if (not line.strip().startswith("ALTER")):
                    if not line.isspace():
                        if line.strip().startswith("CREATE"):
                            i = i + 1;
                            f.write('\n')
                            f.write(('--changeset sudhirg:'+uid+'-1 splitStatements:false ignore').replace(uid+'-1', uid+'-'+str(i)))
                            f.write('\n')
                            if line.strip().startswith("CREATE TABLE"):
                                f.write(line.replace("CREATE TABLE","CREATE TABLE if not exists "))
                            elif line.strip().startswith("CREATE SEQUENCE "):
                                f.write(line.replace("CREATE SEQUENCE ", "CREATE SEQUENCE if not exists "))
                            elif line.strip().startswith("CREATE INDEX "):
                                f.write(line.replace("CREATE INDEX ", "CREATE INDEX if not exists "))
                            else:
                                f.write(line)
                        else:
                            f.write(line)



 #        if '1634807991-1' in line:
 #           i = i + 1;
 #           f.write(line.replace('--changeset yashpanchal:1634807991-1 splitStatements:false','--changeset sudhirg:1634807991-1 splitStatements:false ignore').replace('1634807991-1','1634807991-'+str(i)))
 #       else:
 #           f.write(line)

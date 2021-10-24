f = open("/Users/i1097/Documents/2021_10_22_09_00_SM_integrationv1.sql", "w")
with open('/Users/i1097/Documents/2021_10_22_09_00_SM_integration.sql') as file:
    i = 0
    for line in file:
        # reading each word
        if not line.strip().startswith("--"):
            if line.strip().startswith("CREATE"):
                i = i + 1;
                f.write('\n')
                f.write(('--changeset sudhirg:1634807991-1 splitStatements:false ignore').replace('1634807991-1','1634807991-'+str(i)))
                f.write('\n')
                if line.strip().startswith("CREATE TABLE"):
                    f.write(line.replace("CREATE TABLE","CREATE TABLE if not exists"))
                else:
                    f.write(line)
            else:
                f.write(line)



 #        if '1634807991-1' in line:
 #           i = i + 1;
 #           f.write(line.replace('--changeset yashpanchal:1634807991-1 splitStatements:false','--changeset sudhirg:1634807991-1 splitStatements:false ignore').replace('1634807991-1','1634807991-'+str(i)))
 #       else:
 #           f.write(line)

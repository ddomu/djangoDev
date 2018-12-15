from dbAccess import *
from get_arp import *

# ----- connect DB --- 
try:

    db_conn = MySQLdb.connect(host = db_ip, user= db_usr, passwd = db_passwd, db = vlan_db)
    cur  = db_conn.cursor()
except MySQLdb.Error, e: 
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

   
# ------ get vcmp info ---- # 
query = ("SELECT id, vcmp_ip, site_id  FROM `f5app_f5vcmp` where env_type =%s and tm_type = %s ")
try:
    cur.execute(query,('PROD', 'LTM') )
    vcmps = cur.fetchall()
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


arp_list = [] 
# Test 
#for vcmp in vcmps[0:2]:
for vcmp in vcmps:
    vcmp_id = vcmp[0]
    vcmp_ip = vcmp[1]
    site_id = vcmp[2] 
    ad = get_arp(vcmp_ip) 
    for k,v in ad.iteritems(): 
        arp_ip = k 
        arp_mac = v['mac']
        arp_vlan = v['vlan'].replace('/Common/','')
        arp_status = v['status']
        arp_list.append([arp_ip, arp_mac, arp_vlan, arp_status,site_id,vcmp_id])
    
for i in arp_list:
    print i

# 	---------- INSERT to vlan_table or UPDATE --- # 

m_ins_query = """ 
    		 INSERT INTO f5app_f5arp (arp_ip, arp_mac, arp_vlan, arp_status, site_id, vcmp_name_id, updated) 
			 VALUES (%s,  %s, %s, %s, %s, %s, now()) 
             ON DUPLICATE KEY UPDATE updated = now()
			 """ 
try : 
	cur.executemany (m_ins_query, arp_list) 
	db_conn.commit()
	cur.close()
	db_conn.close()
#	return True 

except MySQLdb.Error, e: 
	print "Error %d: %s" % (e.args[0], e.args[1])
	cur.close()
	db_conn.close()		
#	return False 

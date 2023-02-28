import json

with open('sample.json') as f:
    data = json.load(f)


print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed     MTU")
print("-------------------------------------------------- --------------------  ------  ------") 
for i in data["imdata"]:
    print("{0:50} {1:20} {2:8} {3:^6}".format(i["l1PhysIf"]["attributes"]["dn"],i["l1PhysIf"]["attributes"]["descr"],i["l1PhysIf"]["attributes"]["speed"],i["l1PhysIf"]["attributes"]["mtu"]))
#!/usr/bin/env python

import json, yaml, sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   token = ''
   try:
      opts, args = getopt.getopt(argv,"ht:i:o:",["token","ifile=","ofile="])
   except getopt.GetoptError:
      print 'convert_config.py -t <token> -i <inputfile> -o <outputfile>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'convert_config.py -t <token> -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-t", "--token"):
         token = arg

   with open(inputfile, 'r') as stream:
      try:
         raw = yaml.safe_load(stream)
         clusters = raw["clusters"]
         cluster = clusters[0]["cluster"]
         ca_cert_data = cluster["certificate-authority-data"]
         server = cluster["server"]
         scheme = server.split(":")[0].upper()
         ip_address = server.split(":")[1].replace('//', '')
         port = server.split(":")[2]

         users = raw["users"]
         user = users[0]["user"]
         client_cert_data = user["client-certificate-data"]
         client_key_data = user["client-key-data"]

         api_configs = {
            "scheme": scheme,
            "ipAddress": ip_address,
            "port": int(port),
            "token": token,
            "caCertData": ca_cert_data,
            "clientCertData": client_cert_data,
            "clientKeyData": client_key_data
         }
         data = {
            "apiConfigs": api_configs
         }
      except yaml.YAMLError as exc:
         print(exc)

   # print json.dumps(data)

   with open(outputfile, "w") as jsonfile:
      json.dump(data, jsonfile)

if __name__ == "__main__":
   main(sys.argv[1:])


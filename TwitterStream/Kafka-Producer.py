from kafka import KafkaProducer

#producer = KafkaProducer(bootstrap_servers='sandbox-hdp.hortonworks.com:2181')

producer = KafkaProducer(bootstrap_servers=['sandbox-hdp.hortonworks.com:6667'])

producer.send("trump", "HI I am sayaram")
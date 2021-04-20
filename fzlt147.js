arr1 = ["Kafka", "Apache", "Spark", "Hive"]
arr2 = ["Kafka", "Scala", "Go", "Hive"]
merged = [...new Set([...arr1, ...arr2])]
console.log(merged);//[ 'Kafka', 'Apache', 'Spark', 'Hive', 'Scala', 'Go' ]
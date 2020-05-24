docker run -d --name=elasticsearch -p 9200:9200 -p 9300:9300 -v  ~/Docker/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v ~/Docker/elasticsearch/plugins/elasticsearch-analysis-ik-7.7.0:/usr/share/elasticsearch/plugins/ik683 elasticsearch:7.7.0



测试分词可不可用:
curl -X GET http://localhost:9200/_analyze?pretty -H 'Content-Type:application/json' -d'{ "analyzer": "ik_smart", "text": "　　中新网四川新闻5月23日 电 (杨勇  邓文鑫)记者23日从中国铁路成都局集团公司绵阳车务段获悉，在新冠肺炎疫情防控阻击战中，绵阳车务段立足少数民族职工多的实际，成立以汉、藏、羌、回等多民族职工组成的防疫突 击 队。"}'
说明：
 ik_smart (最少切分) 和 ik_max_word (最细粒度划分)



加索引
curl -H "Content-Type: application/json" -X PUT localhost:9200/?pretty -d '{"name":"_art"}'

docker pull docker.elastic.co/kibana/kibana:7.7.0



php artisan scout:import "App\Models\AddonArticle"

http://localhost:9200/articles/_search
{
    "query": {
        "match": {
            "body": "强人"
        }
    },
   // "sort": { "id": { "order": "desc" }},
    "from": 3,
    "size": 2
}
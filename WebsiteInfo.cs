using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace CynetWebApplication.Models
{
    public class WebsiteInfo
    {
        [BsonId]
        public ObjectId Id { get; set; }

        [BsonElement("url")]
        public string Url { get; set; }

        [BsonElement("div_count")]
        public int DivCount { get; set; }

        [BsonElement("span_count")]
        public int SpanCount { get; set; }

        [BsonElement("links_elements_count")]
        public int LinksElementsCount { get; set; }


        // Parsing the URL to the amount of divs,spans and AElements.
        public WebsiteInfo(string url)
        {
            var htmlWeb = new HtmlAgilityPack.HtmlWeb();
            var doc = htmlWeb.Load(url);
            Id = ObjectId.GenerateNewId();
            Url = url;
            DivCount = doc.DocumentNode.SelectNodes("//div").Count;
            SpanCount = doc.DocumentNode.SelectNodes("//span").Count;
            LinksElementsCount = doc.DocumentNode.SelectNodes("//a").Count;
       
        }
   }
}
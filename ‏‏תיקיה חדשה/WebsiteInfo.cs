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
   }
}
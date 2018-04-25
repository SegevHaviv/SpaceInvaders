using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MongoDB.Driver;
using MongoDB.Bson;

namespace CynetWebApplication.Models
{

    // Wrapper for the MongoClient class.
    public class MongoDBClient : IDBClient
    {
        private readonly MongoUrl mongoUrl = new MongoUrl("mongodb://localhost:27017/cynet");

        // Saves the given WebsiteInfo to the DB
        public void SaveWebsiteInfo(WebsiteInfo websiteInfo)
        {
            var client = new MongoClient(mongoUrl);
            var db = client.GetDatabase(mongoUrl.DatabaseName);

            var coll = db.GetCollection<WebsiteInfo>("websites_data");
            coll.InsertOne(websiteInfo);
        }


        // Retrieves the amount of documents inserted to the DB.
        public long GetDocumnetsCount()
        {
            var client = new MongoClient(mongoUrl);
            var db = client.GetDatabase(mongoUrl.DatabaseName);
 
            var coll = db.GetCollection<WebsiteInfo>("websites_data");
            return coll.Count(Builders<WebsiteInfo>.Filter.Empty);
        }

    }
}
using CynetWebApplication.Models;
using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace CynetWebApplication.Controllers
{
    public class ValuesController : ApiController
    {
        readonly private MongoDBClient mongoClient;
        readonly private WebsiteInfoGateway websiteInfoGateway;

        public ValuesController()
        {
            mongoClient = new MongoDBClient();
            websiteInfoGateway = new WebsiteInfoGateway();
        }

        public long Get()
        {
            return mongoClient.GetDocumnetsCount();
        }

        public void Post([FromBody]WebsiteAnalyzeRequest request)
        {
            var websiteInfo = websiteInfoGateway.WebsiteInfoParser(request.Url);
            mongoClient.SaveWebsiteInfo(websiteInfo);
        }
    }
}

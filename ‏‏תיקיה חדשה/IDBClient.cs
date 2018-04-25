using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CynetWebApplication.Models
{
    interface IDBClient
    {
        void SaveWebsiteInfo(WebsiteInfo websiteInfo);
        long GetDocumnetsCount();
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CynetWebApplication.Models
{
    interface IGateway
    {
        WebsiteInfo WebsiteInfoParser(string url);
    }
}

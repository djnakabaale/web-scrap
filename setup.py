import sys
import json


class SiteMapUrls:
    """ generate start urls to use in the respective sitemap """
    def __init__(self) -> None:
        self.all_states = [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
            "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",  "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        ]

    def get_lawyer_urls(self):
        """ urls to scrape justia.com """
        base_lawyer_url = "https://www.justia.com/lawyers/immigration-law"

        # format urls and replace spaces
        all_lawyers_urls = [
            f"{base_lawyer_url}/dc/washington-dc" if "District of Columbia" == state else f"{base_lawyer_url}/{state.replace(' ', '-').lower()}" for state in self.all_states
        ]
        # save all cleaned urls to text file
        sys.stdout = open('lawyers-justia-urls.txt', 'wt')
        print(json.dumps(all_lawyers_urls))

    def get_ngo_urls(self):
        """ urls to scrape domain: greatnonprofits.org """
        url_prefix = "https://greatnonprofits.org/state"
        url_suffix = "category:Immigration/sort:review_count/direction:desc"

        # format urls and replace spaces
        all_ngo_urls = [
            f"{url_prefix}/{state.replace(' ', '%20')}/{url_suffix}" for state in self.all_states if state
        ]

        # save all cleaned urls to text file
        sys.stdout = open('great-ngo-urls.txt', 'wt')
        print(json.dumps(all_ngo_urls))


if __name__ == "__main__":
    urls = SiteMapUrls()
    urls.get_lawyer_urls()
    urls.get_ngo_urls()
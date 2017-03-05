# Houston
Houston is drop-in-place analytics software for Django projects that stores 100% of usage data in-house. At no point is data sent to third parties.

There are a number of projects in the Django ecosystem that facilitate integration with third party analytics software but most of these entail sending client usage to a third party, most likely Google. This is an acceptable strategy in some cases, Google Analytics is a great product that's easy to integrate with. But if you're developing software where your users might be hesitant to report their every page view to a third party, especially one with a history of illegally disclosing said data, you might want to consider keeping your users' usage data on servers you control.

## Usage
- Add `django-houston` as a dependency in your requirements.txt file
- Add `Houston` to your INSTALLED_APPS setting
- Include the Houston urls at some path in your urls.py file: `url(r'^houston/', include('Houston.urls'))`
- Include the tracking fragment on any pages where views should be tracked: `{% include "Houston/tracking.html" %}`

It's recommended to include the tracking fragment near the end of the document after any page critical scripts to minimize user impact of tracking, although you can include it anywhere.


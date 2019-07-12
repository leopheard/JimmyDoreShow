from xbmcswift2 import Plugin, xbmcgui
from resources.lib import kimiversenshow

plugin = Plugin()

URL = "https://feed.podbean.com/kimiversen/feed.xml"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/ep-logo/pbblog4541467/Untitled-1.jpg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
<<<<<<< HEAD
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/0/4/3/b043eaa3e36ed529/JDPodThumb1.jpg"},
   {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_comedy'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/7/9/5/3/7953b2f961f84fe3/caee-for-podcast.jpg"},

=======
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/ep-logo/pbblog4541467/Untitled-1.jpg"},
>>>>>>> 038dd81bd86778d95a5c90da02264a017375cfa5
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = kimiversenshow.get_soup(URL)
    
    playable_podcast = kimiversenshow.get_playable_podcast(soup)
    
    items = kimiversenshow.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = kimiversenshow.get_soup(URL)
    
    playable_podcast1 = kimiversenshow.get_playable_podcast1(soup)
    
    items = kimiversenshow.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()

import zillow_manager
import poll_manager


zillow_manager = zillow_manager.ZillowManager()
zillow_manager.get_links()
zillow_manager.get_addresses()
zillow_manager.get_prices()

poll_manager = poll_manager.PollManager()
poll_manager.get_web_page()
poll_manager.read_web_file()

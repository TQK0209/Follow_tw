class STwitter:
    def __init__(self, driver,cswait):
        self.driver = driver
        self.cswait = cswait
    def Follow(self,profile_link):
        if self.driver.current_url != profile_link:
            self.driver.get(profile_link)
        return self.cswait.click_by_xpath(20,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div')
    def LikeAndRetweet(self,tweet_link):
        if self.driver.current_url != tweet_link:
            self.driver.get(tweet_link)
        if self.cswait.click_by_xpath(15,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[3]/div[@data-testid="like"]') == 'timeout':
            return {'status': 'error', 'message': 'Error Like tweet: '+tweet_link}
        if self.cswait.click_by_xpath(15,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[2]/div[@data-testid="retweet"]') == 'timeout':
            return {'status': 'error', 'message': 'Error Retweet tweet: '+tweet_link}
        if self.cswait.click_by_xpath(15,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div') == 'timeout':
            return {'status': 'error', 'message': 'Error Retweet tweet: '+tweet_link}
        return {'status': 'success', 'message': 'Successful Retweet tweet: '+tweet_link}
    def RetweetWithQuote(self,tweet_link,quote):
        if self.driver.current_url != tweet_link:
            self.driver.get(tweet_link)
        quote = quote+' '
        if self.cswait.click_by_xpath(20,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[2]/div') == 'timeout':
            return {'status': 'error', 'message': 'Error Retweet with quote tweet: '+tweet_link}
        if self.cswait.click_by_xpath(20,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/a') == 'timeout':
            return {'status': 'error', 'message': 'Error Retweet with quote tweet: '+tweet_link}
        if self.cswait.send_keys_by_xpath(20,'//div[@data-testid="tweetTextarea_0"]',quote) == 'timeout':
            return {'status': 'error', 'message': 'Error Retweet with quote tweet: '+tweet_link}
        if self.cswait.click_by_xpath(20,'//div[@data-testid="tweetButton"]') == 'timeout':
            return {'status': 'error', 'message': 'Error Retweet with quote tweet: '+tweet_link}
        result_link = self.cswait.get_attribute_by_xpath(15,'//*[@id="layers"]/div[2]/div/div/div/div/div[2]/a','href')
        result_link = result_link if result_link!= 'timeout' else 'Can not get link Retweet quote!'
        return {'status': 'success', 'message': 'Successful Retweet with quote tweet: '+tweet_link,'result':result_link}
    def Comment(self,tweet_link,content):
        if self.driver.current_url != tweet_link:
            self.driver.get(tweet_link)
        if self.cswait.click_by_xpath(15,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[1]/div[@data-testid="reply"]') == 'timeout':
            return {'status': 'error', 'message': 'Error Comment tweet: '+tweet_link}
        if self.cswait.send_keys_by_xpath(15,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div',content) == 'timeout':
            return {'status': 'error', 'message': 'Error Comment tweet: '+tweet_link}
        if self.cswait.click_by_xpath(15,'//div[@data-testid="tweetButton"]') == 'timeout':
            return {'status': 'error', 'message': 'Error Comment tweet: '+tweet_link}
        result_link = self.cswait.get_attribute_by_xpath(15,'//*[@id="layers"]/div[2]/div/div/div/div/div[2]/a','href')
        result_link = result_link if result_link!= 'timeout' else 'Can not get link Retweet quote!'
        return {'status': 'success', 'message': 'Successful Comment tweet: '+tweet_link,'result':result_link}

        

        
        
        
        
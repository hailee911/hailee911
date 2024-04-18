import concurrent.futures
import newspaper
from newspaper import Article

URLs = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com', ]  # urls for each news


def get_headlines():
    for url in URLs:
        result = newspaper.build(url, memoize_articles=False)
        print('\n''The headlines from %s are' % url, '\n')  # print headlines
        for i in range(1, 6):  # for loop for each urls
            art = result.articles[i]  # get articles from result
            art.download()  # function from newspaper library
            art.parse()
            print(art.title)  # print the title of the articles


def concur_url():  # concurrent function
    with concurrent.futures.ThreadPoolExecutor(
            max_workers=5) as executor:  # set the workers(thread) to start the thread executor
        future_to_url = {executor.submit(get_headlines)}  # run the function get_headlines


concur_url()

'''Check the elapsed time for getting the headlines for each news'''
if __name__ == '__main__':
    import timeit

    elapsed_time = timeit.timeit("concur_url()", setup="from __main__ import concur_url", number=2) / 2
    print(elapsed_time)

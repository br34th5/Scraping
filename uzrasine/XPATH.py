XPATH

if you want to choose div with a class of intro:
//div[@class='intro']

... and also an element p:
//div[@class='intro']/p

//div[@class='intro' or @class='outro']/p/text()

//a[starts-with(@href, 'https')]

//a[ends-with(@href, 'fr')]

//a[contains(@href, 'google')]
#case sensitive
//a[contains(text(), 'France')]

#selecting whole ul list
//ul[@id='items']

//ul[@id='items']/li[1]

//ul[@id='items']/li[position() >1 or position() = last()]
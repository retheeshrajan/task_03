from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list':[
    	{
    		'restaurant_name':'Ashas',
    		'food_type':'Indian'
    	},
    	{
    		'restaurant_name':'Sakura',
    		'food_type':'Japanese'
    	},
    	{
    		'restaurant_name':'PF Chang',
    		'food_type':'Chinese'
    	}
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object':{
    		'restaurant_name':'Ashas',
    		'food_type':'Indian'
    	}
    }
    return render(request, 'detail.html', context)

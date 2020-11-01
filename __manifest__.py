{
    # Theme information
    'name': "Booking Website",
    'description': """ Website Booking Template
    """,
    'category': 'Theme/corporate',
    'version': '1.0',
    'depends': ['website','website_crm'],

    # templates
    'data': [
	    'views/website_structure/website_page.xml', # views to define website page
	    'views/website_structure/website_menu.xml', # views to define website menu
	    'views/assets/assets.xml', # Load javascript,scss and css on front-End 
        #'views/book_now.xml', # views to define website page
        
		
    ],

    # demo pages
    'demo': [
        'demo/pages.xml',
    ],

    # Your information
    'author': "Teguia polla joel",
	'website': "",
    'sequence':0,
	'active':True,
    'application': True,
    'installable':True,
	
	
	}

**List of implemented APIs** 

###### _Upload User details_

With this operation, a user can be registered with the platform.

~~~
POST /api/accounts/user-profile

Data:

{
    user_name:<user name>
    user_email:<user email>
    user_password:<user password>
    user_description:<user description>
}
~~~

###### _Retrieve User details_

With this operation, a registered user's details can be retrieved. 

~~~
GET /api/accounts/user-profile
~~~

###### _Upload Advertiser details_

With this operation, advertiser's details can be registered with the platform.
~~~
POST /api/accounts/advertiser-profile

Data:

{
    advertiser_name:<advertiser name>
    advertiser_password:<advertiser password>
    advertiser_email:<advertiser email>
}
~~~

###### _Retrieve Advertiser details_

With this operation, advertiser's details can be retrieved with the platform.

~~~
GET /api/accounts/advertiser-profile
~~~


###### _Upload advertiser logo_

With this operation, advertiser can upload the logo that needs to be used
for advertising.

~~~
POST /record/upload-image/

Data:

image : <image file attached>
image_property_id: 1
~~~

###### _Upload advertiser Text_

With this operation, advertiser can upload the logo that needs to be used
for advertising.

~~~
POST /record/upload-text/

Data:

text: <text to be sent in string format>
text_property_id: <same as image_property_id>

~~~

###### _Retrieve phase Asset_

With this operation, ad asset can be retrieved after 
the proprietary algorithm runs on the platform.

~~~
GET /api/v1/FetchAsset

Data:

Advertiser: <advertiser name previously registered>
user_email: <user email previously registered>

~~~

###### _Retrieve phase Profile_

With this operation, current phase where the user as well as advertiser is standing
can be retrieved.

~~~
GET /api/accounts/phase-profile
~~~







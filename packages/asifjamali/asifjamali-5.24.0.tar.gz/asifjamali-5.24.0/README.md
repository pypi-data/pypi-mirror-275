# MusibaT #


# What is this repository for? #

* Learning Perpose
* Version 0.2.1
* [Learn iSsues](https://bitbucket.org/shahzain83/musibat/issues)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

# mid url #
* xx = shahzi.getinfo(usrmid)
* print(xx)

# name short #
* xx = shahzi.makeName(usrmid)
* print(xx)

# translator #
* query = "how are you ?"
# if wanna trans arabic #
* trTo = "ar"
# if wanna trans urdu #
* trTo = "ur"
* oText = shahzi.TransLangs(trTo, query)
* print(oText)

# fix Plain text error #
* if wait["upOnce"] == True:
*     shahzi.fixPlaining(noobcoderMID, noobcoder)
*     wait["upOnce"] = False

# clear cache #
* shahzi.clearVpscache()

# Login method #
* reQR = shahzi.LineGetQr(appname)
* print(reQR)
* pincode = shahzi.lineGetQrPincode(reQR["result"]["session"])
* print(pincode)
* auth = shahzi.lineGetQrAuth(reQR["result"]["session"])
* print(auth)

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Contact Line ###

* musibat_bots
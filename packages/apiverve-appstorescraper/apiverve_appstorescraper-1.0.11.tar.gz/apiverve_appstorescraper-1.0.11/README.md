App Store Scraper API
============

App Store Scraper is a simple tool for scraping app store data. It returns the app name, description, price, and more.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [App Store Scraper API](https://apiverve.com/marketplace/api/appstorescraper)

---

## Installation
	pip install apiverve-appstorescraper

---

## Configuration

Before using the appstorescraper API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The App Store Scraper API documentation is found here: [https://docs.apiverve.com/api/appstorescraper](https://docs.apiverve.com/api/appstorescraper).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_appstorescraper.apiClient import AppstorescraperAPIClient

# Initialize the client with your APIVerve API key
api = AppstorescraperAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "appid": "553834731",  "country": "us" }
```

###### Simple Request

```
# Make a request to the API
result = api.execute(query)

# Print the result
print(result)
```

###### Example Response

```
{
  "status": "ok",
  "error": null,
  "data": {
    "id": 553834731,
    "appId": "com.midasplayer.apps.candycrushsaga",
    "title": "Candy Crush Saga",
    "url": "https://apps.apple.com/us/app/candy-crush-saga/id553834731?uo=4",
    "description": "Start playing Candy Crush Saga today – a legendary puzzle game loved by millions of players around the world.  With over a trillion levels played, this sweet match 3 puzzle game is one of the most popular mobile games of all time!  Switch and match Candies in this tasty puzzle adventure to progress to the next level for that sweet winning feeling! Solve puzzles with quick thinking and smart moves, and be rewarded with delicious rainbow-colored cascades and tasty candy combos!  Plan your moves by matching 3 or more candies in a row, using boosters wisely in order to overcome those extra sticky puzzles! Blast the chocolate and collect sweet candy across thousands of levels, guaranteed to have you craving more!  Candy Crush Saga features:  THE GAME THAT KEEPS YOU CRAVING MORE Thousands of the best levels and puzzles in the Candy Kingdom and with more added every 2 weeks your sugar fix is never far away!   MANY WAYS TO WIN REWARDS Check back daily and spin the Daily Booster Wheel to receive free tasty rewards, and take part in time limited challenges to earn boosters to help you level up!    VARIETY OF SUGAR-COATED CHALLENGES Sweet ways to play: Game modes including Target Score, Clear the Jelly, Collect the Ingredients and Order Mode  PLAY ALONE OR WITH FRIENDS Get to the top of the leaderboard events and compare scores with friends and competitors!  Levels range from easy to hard for all adults to enjoy – accessible on-the-go, offline and online. It's easy to sync the game between devices and unlock full game features when connected to the Internet or Wifi. Follow us to get news and updates; facebook.com/CandyCrushSaga, Twitter @CandyCrushSaga, Youtube https://www.youtube.com/user/CandyCrushOfficial Visit https://community.king.com/en/candy-crush-saga to access the Community and competitions! Candy Crush Saga is completely free to play but some optional in-game items will require payment. You can turn off the payment feature by disabling in-app purchases in your device’s settings. By downloading this game you are agreeing to our terms of service; http://about.king.com/consumer-terms/terms  Do not sell my data: King shares your personal information with advertising partners to personalize ads. Learn more at https://king.com/privacyPolicy.  If you wish to exercise your Do Not Sell My Data rights, you can do so by contacting us via the in game help centre or by going to https://soporto.king.com/  Have fun playing Candy Crush Saga the sweetest match 3 puzzle game around!   If you enjoy playing Candy Crush Saga, you may also enjoy its sister puzzle games; Candy Crush Soda Saga, Candy Crush Jelly Saga and Candy Crush Friends Saga!  All Stars Tournament Selected level 25+. 18+. In-game tournament 09:00 EDT 28th March - 09:00 EDT 28th April 2024. Participating countries only. Win the in-game tournament and receive an invite to the live contest in California, June 2024. Requires US travel. T&Cs: candycrush-saga.web.app/pages/all_stars_terms. © 2024 King.com Ltd.",
    "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/59/03/9a/59039ab7-c230-3e44-0a1f-1d56d127e1f2/AppIcon-0-0-1x_U007emarketing-0-7-0-85-220.png/512x512bb.jpg",
    "genres": [
      "Games",
      "Entertainment",
      "Puzzle",
      "Casual"
    ],
    "genreIds": [
      "6014",
      "6016",
      "7012",
      "7003"
    ],
    "primaryGenre": "Games",
    "primaryGenreId": 6014,
    "contentRating": "4+",
    "languages": [
      "AR",
      "CA",
      "HR",
      "CS",
      "DA",
      "NL",
      "EN",
      "FI",
      "FR",
      "DE",
      "HU",
      "ID",
      "IT",
      "JA",
      "KO",
      "MS",
      "NB",
      "PL",
      "PT",
      "RO",
      "RU",
      "ZH",
      "SK",
      "ES",
      "SV",
      "TH",
      "ZH",
      "TR",
      "VI"
    ],
    "size": "359188480",
    "requiredOsVersion": "12.0.0",
    "released": "2012-11-14T14:41:32Z",
    "updated": "2024-05-08T05:36:28Z",
    "version": "1.277.0.2",
    "price": 0,
    "currency": "USD",
    "free": true,
    "developerId": 526656015,
    "developer": "King",
    "developerUrl": "https://apps.apple.com/us/developer/king/id526656015?uo=4",
    "developerWebsite": "http://candycrushsaga.com/",
    "score": 4.70614,
    "reviews": 3233691,
    "currentVersionScore": 4.70614,
    "currentVersionReviews": 3233691,
    "screenshots": [
      "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/cf/e3/03/cfe303a7-e326-c820-0e90-bff6c6636ca4/984b2f1b-2c41-4dbb-80f7-345470b7dbc5__sta_ios-6s_1242x2208_1.png/392x696bb.png",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/16/75/23/167523ad-380d-8502-992d-c28db14ae247/66fb12f9-e3d4-4234-a862-ca1a3514f0e7_285580_ccs_store-revamp_sta_ios-6s_1242x2208_2_en.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/04/0f/f8/040ff86e-3733-be3b-1b65-64603208dfeb/bfc11de4-80ed-4522-8c53-88ce9d6e5d0b_285580_ccs_store-revamp_sta_ios-6s_1242x2208_3_en.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/4b/a2/5f/4ba25f47-96a6-0b84-e8d1-e7de01fc61d6/6e592b00-08b7-41d4-a7ca-21becdba397c_285580_ccs_store-revamp_sta_ios-6s_1242x2208_4_en.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/7f/8a/e1/7f8ae16d-e996-a131-2c1a-6d4ef4cd65d5/14163e37-4d5d-47be-999e-5d0383be9fd1_285580_ccs_store-revamp_sta_ios-6s_1242x2208_5_en.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/8b/22/91/8b2291c7-755d-e51d-7021-7d8ae07fe25e/e780ff64-d670-4b71-8543-afe8b0fdc6fe_513402_CCS_allstars24_Screenshots_Jan_24_sta_ios-6s_1242x2208_1.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/1a/56/5b/1a565b8e-e396-d190-479b-375d18a2cce8/e8161bd0-89f5-4dd0-b725-f04922f194e8_285580_ccs_lt_aso-true-to-gameplay-ss_sta_ios-6s_1242x2208_1.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/b6/18/a1/b618a103-6826-f6c2-e9de-d7b619612ab5/feece3b7-0e98-44f6-a410-c0839c5f023c_285580_ccs_lt_aso-true-to-gameplay-ss_sta_ios-6s_1242x2208_2.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/80/ce/39/80ce399c-dec5-c8d9-3d71-ff8e1707df76/4566515f-0e05-46e9-a782-2075a59941a5_285580_ccs_lt_aso-true-to-gameplay-ss_sta_ios-6s_1242x2208_3.jpg/392x696bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/75/ce/c7/75cec72a-813a-2797-70b5-c008583f9724/22e89292-8124-4f09-9788-3995305da759_364295_CCS_Saga-Map-Update_ss_1242x2208_en.jpg/392x696bb.jpg"
    ],
    "ipadScreenshots": [
      "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/40/75/c0/4075c01b-fa5b-1fb1-85da-1b4b1c883ae6/ee017145-486f-4a26-b73c-b0a5ffc4f150_498713_ASO_CCS_Night_Sky_Candies_Screenshot_Resizes_Dec_23_sta_ios-iPad_2048x2732_1.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/03/b2/8c/03b28cca-c72f-98e1-90ae-fdb15bbfffd2/0375e811-aa00-4f5b-ab64-545dc5e4c223_285580_ccs_store-revamp_sta_ios-iPad_2048x2732_2_en.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ce/bc/e2/cebce2e5-e724-634e-b2e4-8f213728b73c/c8de8e8d-d7f2-4b2f-9dae-9abe2dacc682_285580_ccs_store-revamp_sta_ios-iPad_2048x2732_3_en.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/11/d1/7d/11d17d74-16cc-2564-b9c8-6a183431293b/cec7f27b-1f97-4eb9-a578-b4a1970e4424_285580_ccs_store-revamp_sta_ios-iPad_2048x2732_4_en.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/31/8f/e3/318fe3f3-2059-9d89-2ab3-2fd62fac221e/482c13df-fffa-40a5-959b-52cc99d057b5_285580_ccs_store-revamp_sta_ios-iPad_2048x2732_5_en.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource122/v4/84/19/2b/84192b79-5a96-f86b-8d62-cd6a5bc294bc/cc5dd657-9c86-4323-82d4-06971f0a5a4f_513402_CCS_allstars24_Screenshots_Jan_24_sta_ios-iPad_2048x2732_3.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/5a/ce/91/5ace9173-8a34-1b37-2193-2bdcee28ce28/43dbc8a0-5f8c-4f42-ad4b-9de28521386a_285580_ccs_lt_aso-true-to-gameplay-ss_sta_ios-iPad_2048x2732_1.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e3/cb/39/e3cb3980-12ee-6c75-0513-19d153878a7c/96b029b6-7822-4ed5-8367-552646806b1b_285580_ccs_lt_aso-true-to-gameplay-ss_sta_ios-iPad_2048x2732_2.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/a2/97/13/a297138f-ab5b-6fdc-54c9-779d8cdf48bb/835e9d44-e4b3-4f74-b6f0-a01a8f1f0ec3_285580_ccs_lt_aso-true-to-gameplay-ss_sta_ios-iPad_2048x2732_3.jpg/576x768bb.jpg",
      "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/47/5e/b0/475eb0a9-4f98-83d5-f80d-45eb1cebf1e8/d1c5f541-5d59-4cb6-abf7-b9d68d943277_364295_CCS_Saga-Map-Update_ss_2048x2732_en.jpg/576x768bb.jpg"
    ],
    "appletvScreenshots": [],
    "supportedDevices": [
      "iPhone5s-iPhone5s",
      "iPadAir-iPadAir",
      "iPadAirCellular-iPadAirCellular",
      "iPadMiniRetina-iPadMiniRetina",
      "iPadMiniRetinaCellular-iPadMiniRetinaCellular",
      "iPhone6-iPhone6",
      "iPhone6Plus-iPhone6Plus",
      "iPadAir2-iPadAir2",
      "iPadAir2Cellular-iPadAir2Cellular",
      "iPadMini3-iPadMini3",
      "iPadMini3Cellular-iPadMini3Cellular",
      "iPodTouchSixthGen-iPodTouchSixthGen",
      "iPhone6s-iPhone6s",
      "iPhone6sPlus-iPhone6sPlus",
      "iPadMini4-iPadMini4",
      "iPadMini4Cellular-iPadMini4Cellular",
      "iPadPro-iPadPro",
      "iPadProCellular-iPadProCellular",
      "iPadPro97-iPadPro97",
      "iPadPro97Cellular-iPadPro97Cellular",
      "iPhoneSE-iPhoneSE",
      "iPhone7-iPhone7",
      "iPhone7Plus-iPhone7Plus",
      "iPad611-iPad611",
      "iPad612-iPad612",
      "iPad71-iPad71",
      "iPad72-iPad72",
      "iPad73-iPad73",
      "iPad74-iPad74",
      "iPhone8-iPhone8",
      "iPhone8Plus-iPhone8Plus",
      "iPhoneX-iPhoneX",
      "iPad75-iPad75",
      "iPad76-iPad76",
      "iPhoneXS-iPhoneXS",
      "iPhoneXSMax-iPhoneXSMax",
      "iPhoneXR-iPhoneXR",
      "iPad812-iPad812",
      "iPad834-iPad834",
      "iPad856-iPad856",
      "iPad878-iPad878",
      "iPadMini5-iPadMini5",
      "iPadMini5Cellular-iPadMini5Cellular",
      "iPadAir3-iPadAir3",
      "iPadAir3Cellular-iPadAir3Cellular",
      "iPodTouchSeventhGen-iPodTouchSeventhGen",
      "iPhone11-iPhone11",
      "iPhone11Pro-iPhone11Pro",
      "iPadSeventhGen-iPadSeventhGen",
      "iPadSeventhGenCellular-iPadSeventhGenCellular",
      "iPhone11ProMax-iPhone11ProMax",
      "iPhoneSESecondGen-iPhoneSESecondGen",
      "iPadProSecondGen-iPadProSecondGen",
      "iPadProSecondGenCellular-iPadProSecondGenCellular",
      "iPadProFourthGen-iPadProFourthGen",
      "iPadProFourthGenCellular-iPadProFourthGenCellular",
      "iPhone12Mini-iPhone12Mini",
      "iPhone12-iPhone12",
      "iPhone12Pro-iPhone12Pro",
      "iPhone12ProMax-iPhone12ProMax",
      "iPadAir4-iPadAir4",
      "iPadAir4Cellular-iPadAir4Cellular",
      "iPadEighthGen-iPadEighthGen",
      "iPadEighthGenCellular-iPadEighthGenCellular",
      "iPadProThirdGen-iPadProThirdGen",
      "iPadProThirdGenCellular-iPadProThirdGenCellular",
      "iPadProFifthGen-iPadProFifthGen",
      "iPadProFifthGenCellular-iPadProFifthGenCellular",
      "iPhone13Pro-iPhone13Pro",
      "iPhone13ProMax-iPhone13ProMax",
      "iPhone13Mini-iPhone13Mini",
      "iPhone13-iPhone13",
      "iPadMiniSixthGen-iPadMiniSixthGen",
      "iPadMiniSixthGenCellular-iPadMiniSixthGenCellular",
      "iPadNinthGen-iPadNinthGen",
      "iPadNinthGenCellular-iPadNinthGenCellular",
      "iPhoneSEThirdGen-iPhoneSEThirdGen",
      "iPadAirFifthGen-iPadAirFifthGen",
      "iPadAirFifthGenCellular-iPadAirFifthGenCellular",
      "iPhone14-iPhone14",
      "iPhone14Plus-iPhone14Plus",
      "iPhone14Pro-iPhone14Pro",
      "iPhone14ProMax-iPhone14ProMax",
      "iPadTenthGen-iPadTenthGen",
      "iPadTenthGenCellular-iPadTenthGenCellular",
      "iPadPro11FourthGen-iPadPro11FourthGen",
      "iPadPro11FourthGenCellular-iPadPro11FourthGenCellular",
      "iPadProSixthGen-iPadProSixthGen",
      "iPadProSixthGenCellular-iPadProSixthGenCellular",
      "iPhone15-iPhone15",
      "iPhone15Plus-iPhone15Plus",
      "iPhone15Pro-iPhone15Pro",
      "iPhone15ProMax-iPhone15ProMax"
    ]
  }
}
```

---

## Customer Support

Need any assistance? [Get in touch with Customer Support](https://apiverve.com/contact).

---

## Updates
Stay up to date by following [@apiverveHQ](https://twitter.com/apiverveHQ) on Twitter.

---

## Legal

All usage of the APIVerve website, API, and services is subject to the [APIVerve Terms of Service](https://apiverve.com/terms) and all legal documents and agreements.

---

## License
Licensed under the The MIT License (MIT)

Copyright (&copy;) 2024 APIVerve, and Evlar LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
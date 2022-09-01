import json
import os
import requests
from datetime import datetime

# import logging

# import logging

# logging.basicConfig(filename='data.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def extract():

    headers = {
        "authority": "api.nike.com",
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "cookie": 'AnalysisUserId=2.17.35.103.162441661528390989; geoloc=cc=NG,rc=,tp=vhigh,tz=GMT+1,la=6.45,lo=3.40; s_ecid=MCMID%7C30765560244911791645617054311885057217; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C30765560244911791645617054311885057217%7CMCAID%7CNONE%7CMCOPTOUT-1661535610s%7CNONE%7CvVersion%7C3.4.0; CONSUMERCHOICE_SESSION=t; anonymousId=4BDA24CABADC363265C54C3502599558; guidS=a7732c7f-ce66-41b5-c074-7a1291fba652; guidU=7abee57f-4bd9-47f7-bf4b-4cf771ee37fc; RES_TRACKINGID=177063899674295; ResonanceSegment=1; _gcl_au=1.1.1052584455.1661528616; _ga_EWJ8FE8V0B=GS1.1.1661528619.1.0.1661528619.60.0.0; _scid=0e13098d-ddfe-4f2c-9452-5358cc66130b; _uetvid=21039f70e44911ec8e5b277899d64d47; bc_nike_south_africa_triggermail=%7B%22distinct_id%22%3A%20%22181308368b35a3-05651c99bdca38-26021b51-100200-181308368b4175%22%2C%22bc_persist_updated%22%3A%201661528622482%2C%22cart_total%22%3A%200%7D; _fbp=fb.1.1661528633125.2110745594; _derived_epik=dj0yJnU9Q05vU2pnb3k2WFliUzlGRl9iaDNTOHd0Y2NSNHdUTDImbj0zNFJRY1JhZkhhUFJEcWR5S2NzNzdnJm09MSZ0PUFBQUFBR01JNmxnJnJtPTEmcnQ9QUFBQUFHTUk2bGc; _pin_unauth=dWlkPU9HTTVaV1JpTnpndE1qY3laaTAwTVdSbExXRmhObVV0WXpkbVl6WXlObVkwWmpFNQ; optimizelyEndUserId=oeu1661537925297r0.42743005943276535; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; nike_locale=us/en_us; CONSUMERCHOICE=us/en_us; cid=undefined%7Cundefined; AKA_A2=A; feature_enabled__as_nav_rollout=true; audience_segmentation_performed=true; bm_sz=21602494DA0804B96A21AE91F88B493A~YAAQXCMRAlDFBsmCAQAAX9Qm8BDUubc1KrnWUSnjepw7ZS8R0GjH+pLvcf6ky8+TKjNASwKBXB4rPjauCvbY98h0Dlypabn/OxjSP+fxMfi9ATaA8P8GGCdUhIVmu8NrqpCvoXmbHU9OkYfaG7SAklYQAj0YsagWxgP9Tr6dJVRrF5S7BWI+mqeOlGDOCKde37INU7SUyOt8q7cjv8skn85M+WfDTet8FXoDs0RQ3ZSAq1ZYaP/BKENjzjNZnq+r34RjwJVVPMRZgxuQ08pW4kUrYyWZDIca0bGRxbECj0zR5udkILu7UMkmU+4nTU/WnFVSgssLA2ekqnC9OgcfsA39SqISO/LluKGG+5qqeIXtGvUpC24inQYoEkaA16+FEW6FWL/pGTTsMDibg8VDf50=~3359028~3359792; bm_mi=963E606A63E2FBFCE06DF631EBD2ADCE~YAAQdNMRAv1s3cqCAQAAyAwn8BCHuTcH25gVE5/l3JWkiRuRo0/dUUmvgHUcmW4aMnnWopGY61qjc6oFFvNxnGblt7Xl/kp9yfY2+jVVGW4sX5TY8c6ps8ku3uxIWZ3vj7yQ6M50K8UtDlhIjWPar4DpZWvp2y5iAQMGE4sVGIPpxlM87o30kjCrkPr8c++pdp3hz9EtJXvGVn+UZumh5tC4sklFjWomfC9xBRBlMZ7dI/rulsNdtY0JUOotCvshFmUpfkENZvQyaNzzmj5zkA4pHG9n6m6IDpfFyKHugbZURvxId6xx7E9f/Lp0kFUZM/RJU6swIg==~1; ak_bmsc=E4FF74964815637F69687282269A214D~000000000000000000000000000000~YAAQdNMRArht3cqCAQAAphIn8BAv7DN+N0oFX5zMpaW1uboI2B/exnACLB7OfK59z8np9tzRkp5ShDtDPAxj4GEa60I834UfLb+UxD7lLopvmJSXCIrGnYS9AK/CUqRXhHYcFYikl9UwUYCnlGhx2oOh8MdGDZqiNimYB4v/6GLOv6YbLq7J9MBVJ19O3VRTSrky9DUs3H4gIgmScDtByEpvjD99qeGH0aPtrsNVa/phrj5J4Rmdn9guBvVKXmzlzEWttghCUJ1aqg7PEJrUQhe4uEtWQmipz5JsqjosLvZi9M4+qj1m/WX2LvMcV971RsC+e3fOfjOLja/XsCnrR+p3BueES5AJzGX17am+EzI15IS7e5CGWZEmG7kSJZ5KucGP197pds+cqZxDItArQmSBllNS/ZwONHJLayUILXklYYVHLRo1IK8SGBdi3UvzjOcJwcHBf7x0JEsWiyWaNagc9eyoqZ9SIopi0umbp//ILhs4nibr93Nw/n/dYcjo9ZCGw47HMeI7+lqe; _gid=GA1.2.1491211993.1661886491; ak_bmsc_nke-2.2-ssn=09vL9KIQgz9XpARGetLM5MbpOhKOsDp864QlvunLmNKRX1pHJaS3qBPrZguUAofaTemojSDALINRYZJ1k0jt6Uu6bH1wsOblkKqE3yHju68phLA7FAgAs4z73TxxpR1QENnjPTnH5iZdVp9W8Yot3FL3T3FP; ak_bmsc_nke-2.2=09vL9KIQgz9XpARGetLM5MbpOhKOsDp864QlvunLmNKRX1pHJaS3qBPrZguUAofaTemojSDALINRYZJ1k0jt6Uu6bH1wsOblkKqE3yHju68phLA7FAgAs4z73TxxpR1QENnjPTnH5iZdVp9W8Yot3FL3T3FP; ppd=onsite%20search|nikecom>onsite%20search>results%20found; RT="z=1&dm=nike.com&si=6cbe15e7-0396-41f5-96be-7db73f88bf3c&ss=l7gkxwcm&sl=5&tt=2g64&obo=1&bcn=%2F%2F0217990f.akstat.io%2F&ld=zhn"; bm_sv=F7A386DC50C0F2B50F25D8EFAC35EA92~YAAQXCMRAmyECMmCAQAAYXs48BCDKDE8jIa4XShwlx3AvIi52Ik8dfzQxDyeOPYBZ6K/K43saC6yleW+6dfz6dDWU9ByFUPPLh/ZVLjzzJv4RR/Lo3j3POeGfK2glzu058ZeIumJf00UEKX+GReHvMBQZoYnS5i7Upc61ToEK4esZi503uKmH86K/VSBzm73wyoyHK6rngiJOgdjdTCLb37Ua7euVnWsHgK8HRhL63hoS0yapHgZtxDgJwRJbLU=~1; _ga=GA1.1.831967198.1661528619; _ga_QTVTHYLBQS=GS1.1.1661886494.4.1.1661887615.59.0.0; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%22181308368b35a3-05651c99bdca38-26021b51-100200-181308368b4175%22%2C%22bc_persist_updated%22%3A%201661558814075%2C%22cart_total%22%3A%200%2C%22g_search_engine%22%3A%20%22google%22%7D; cto_bundle=-NZR6F9PQ0NKRUdnSGM5JTJGWWYwcjd5eld5OGV6cllMYUg1d1JRUVhocnI5V1ZmcVh3Q29qbkQ2ZUdSSXJwcUdOdjBxRnRVRzBPd3ZpJTJGMDZ6OE81MHQyVDRaQXRYMjFNN1R3STVycjg5QzhGUTVJVFFTdVF4Sm9ycXJNRG5KRDk5dHA5cGtHODVIUTRwbnpRaDFuV2V4bHNWWkF3JTNEJTNE; _abck=303E7C53F86665F74B2B6E5716887EFD~-1~YAAQRm9WaCZPvM2CAQAAxzs68AiC5hTjM0gbQRBuGztf8h1Q1wI8Dz3bUZXd3T7mJXO1ek1EE8QpvrkH/v/gxnKtn/Yv8g61pHUivawy1cEYvKNIWAHCvCxBgRpeIKZVGGNPHmPH0cGspEgLSd1RGcEMqh3+We7DI2nJOGKxtySU4xfZvDxbNDdHAn3NgPsBfxT7O9GI8fpfwsnNOTzzhqLbvM9t6sISDUFvniRkiRogR1dibY04O8S5XwlVD0nB/n6USP2wPtK0LqS1F35ge8ToJcLL0qUJ6ror610Yy4rBTYVizDPpe0JTKHu+6g9Qd+wh3dm61c7DkR20Sigo2ztu4INkpHP2fxcFnQeKIhvWgzknnSq9JZG4zgdly623U/T2pwekmcEt7LyHOSGx+Sc+7gcjpXR7GlQRomS+1B8Y1cZ+XidErRPaNBOpVJPb0rPMVsXWH3uwvvjy5gFmeLTBMLUp8iYIEIhek6Pf/foD7v4OgxOs2O0OiPDIO1ITmSbqZvaoE74+2Fcr++SCV3yTmq5W+O8=~-1~-1~-1; _abck=303E7C53F86665F74B2B6E5716887EFD~-1~YAAQztMRAtDM4siCAQAAYoQ78AiD1KYTKexjfC4XTDdb08OAS0fwQqpGs/snWXyh/Hb5zyk5rusfdqqaHvzoM9q195ZT3R4gEyRs7wmO+EaCOLoetmpYlRJcKeVEcNonKMVYEvDD2jNXd4bHkQeIsm+xG0eJVaQsxTC43zZFan09QcMv3763xubaRY5cCFsUoW5LPOV1viTSmeiqY7GSsY/GIXiQSHs6rxVXbZEiKPEUaDN415Fn1wpoM2inPOXZHvfBcK4HTTHysCaBJXcoz7PG2/hyuf4xM94ClJVMSFmkeSILcjCKWWem2T4IkbmDMuWJYSAsbrZhjsejlNSKFMvEilV9Sw1XVEgBx/LYQA+PSK3m1zczXeMHHCBAnQWSnb9ONj16v+8anXAy+EnBJKalN3T4mJEIpvUylK6+3lrBQMZOP/rGODY25cqdT/Y7bxOJBY+/jYBYaYlaGaalHqJdlWQms2kqWfFYkN6kc1fgWhWQ4Zr/15Y+1oI/AwibHqd1lb72ezmjvJp5P4rLDTex9rgaUGI=~0~-1~-1',
        "origin": "https://www.nike.com",
        "pragma": "no-cache",
        "referer": "https://www.nike.com/",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }

    count = 60
    step = 1

    curr = os.getcwd
    data_dir = os.path.join(curr, "data")

    for anchor in range(60, 1440, 60):
        url = f"https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=4BDA24CABADC363265C54C3502599558&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26searchTerms%3Dsneakers%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{count}&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D"

        print(f"Start : Anchor {anchor}")
        response = requests.get(url, headers=headers)
        result = response.json()
        print(type(result))

        filename = f"nike-{datetime.now().strftime('%d-%m-%Y')}-anchor-{anchor}.json"
        with open(f"{data_dir}/{filename}", "w", encoding="utf-8") as f:
            json.dump(result, f)

        print(f"Step {step} Done!!!")

        step += 1

if __name__ == "__main__":
    extract()
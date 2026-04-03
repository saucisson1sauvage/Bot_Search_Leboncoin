
import statistics
import sys
import lbc

# recherche sur leboncoin qui retourne tout ce dont on need
def search_lbc(item_name):
    client = lbc.Client()
    response = client.search(text=item_name)
    
    results = []
    # extraction titre prix et lien
    for ad in response.ads:
        if ad.subject is None or ad.price is None or ad.url is None:
            continue

        item = {
            "title": ad.subject,
            "price": float(ad.price),
            "url": ad.url,
        }
        results.append(item)

    return results

# fonction pr print les resultats et les stats
def show_results(results):
    # Sécurité au cas où aucun article n'est trouvé
    if not results:
        print("\nAucun résultat trouvé sur Leboncoin.")
        return

    prix = []
    for item in results:
        prix.append(item["price"])
        # calcul stats
        
    average = statistics.mean(prix)
    median = statistics.median(prix)
    lowest = min(results, key=lambda item: item["price"])
    difference = average - lowest["price"]

# check non nul & calcul pourcentage
    if average != 0:
        percent = (difference / average) * 100
    else:
        percent = 0
        
# print de tout        
    print("\nPrix trouvés:")
    for item in results:
        print(f"- {item['title']}")
        print(f"  Prix: {item['price']:.2f} €")
        print(f"  Lien : {item['url']}")

    print(f"\nAverage : {average:.2f} €")
    print(f"Median : {median:.2f} €")
    print("Moins cher:")
    print(f"- Item : {lowest['title']}")
    print(f"- Prix: {lowest['price']:.2f} €")
    print(f"- Lien : {lowest['url']}")
    print(f"\nDiff entre moins cher et +cher: {difference:.2f} €")
    print(f"Difference en % : {percent:.2f}%")

def main():
    # check si on donne bien un argument sinon on ask
    if len(sys.argv) > 1:
        item_name = ""
        i = 1
        while i < len(sys.argv):
            if item_name != "":
                item_name = item_name + " "
            item_name = item_name + sys.argv[i]
            i = i + 1
    else:
        item_name = input("item recherché : ").strip()

    results = search_lbc(item_name)
    show_results(results)

if __name__ == "__main__":
    main()

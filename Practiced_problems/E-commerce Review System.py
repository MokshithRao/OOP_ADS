class Review:
    def __init__(self, reviewID, productID, reviewText, rating) -> None:
        self.reviewID = reviewID
        self.ProductID = productID
        self.reviewText = reviewText
        self.rating = rating


    def getReviewSummary(self):
        return f"{self.reviewText}, {self.rating}"
    


class Product:
    def __init__(self, productID, name, price) -> None:
        self.productID = productID
        self.name = name
        self.price = price

    def getProductInfo(self):
        return f"{self.name}, {self.price}"
    


class ReviewManager:
    def __init__(self, reviews) -> None:
        self.reviews = reviews

    def addReview(self, review):
        self.reviews.append(review)
    
    def getReviewsByProduct(self, productID):
        return self.reviews








def main():
    # Create reviews
    review1 = Review(1, 101, "Great product!", 5)
    review2 = Review(2, 101, "Not bad", 4)
    review3 = Review(3, 102, "Poor quality", 2)

    # Create products
    product1 = Product(101, "Smart Watch", 199.99)
    product2 = Product(102, "Fitness Tracker", 99.99)

    # Create ReviewManager and add reviews
    rm = ReviewManager([])
    rm.addReview(review1)
    rm.addReview(review2)
    rm.addReview(review3)

    # Display reviews for product1 and product2
    print("Reviews for product 101:")
    for r in rm.getReviewsByProduct(101):
        print(r.getReviewSummary())
    print("Reviews for product 102:")
    for r in rm.getReviewsByProduct(102):
        print(r.getReviewSummary())

    # Display product info
    print("Product 101 info:", product1.getProductInfo())
    print("Product 102 info:", product2.getProductInfo())

if __name__ == '__main__':
    main()
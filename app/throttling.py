from rest_framework.throttling import UserRateThrottle

class CategoryThrottle(UserRateThrottle):
    scope = 'category'

class DishThrottle(UserRateThrottle):
    scope = 'dish'

class ReviewThrottle(UserRateThrottle):
    scope = 'review'

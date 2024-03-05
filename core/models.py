from django.db import models

from accounts.models import CustomUser


class Institute(models.Model):
    """
    Model representing an institute.
    """

    name = models.CharField(max_length=255)

    # Add any additional fields specific to institutes, for example:
    # address = models.CharField(max_length=255, blank=True)
    # website = models.URLField(blank=True)
    def __str__(self):
        return self.name


class Plan(models.Model):
    """
    Model representing a plan offered by an institute.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.institute.name})"


class UserPlan(models.Model):
    """
    Model representing a relationship between a user and a plan, tracking payments and active status.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(
        auto_now_add=True
    )  # Date the plan subscription started

    # Track active status:
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            "user",
            "plan",
        )  # Enforces unique subscription per user-plan combo
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.user} - {self.plan.name} ({'Active' if self.is_active else 'Inactive'})"


class Payment(models.Model):
    """
    Model representing a user's monthly payment for a UserPlan.
    """

    user_plan = models.ForeignKey(UserPlan, on_delete=models.CASCADE)
    payment_date = models.DateField(
        auto_now_add=True
    )  # Date the payment was made
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.user_plan}: ${self.amount} on {self.payment_date}"

    # @classmethod
    # def create_payment(cls, user_plan, amount):
    #     """
    #     Creates a new payment record for the given UserPlan with the specified amount.
    #     """
    #     payment = cls.objects.create(user_plan=user_plan, amount=amount)
    #     return payment

from django.db.models import Subquery
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.carts.carts import Cart


class StudentsDashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboards/student_dashboard.html'
    
    def get(self, request):
        cart = Cart(request)
        total_price, total_discounted_price = cart.get_total_price()

        context = {
            'carts': cart,
            'total_price': total_price,
            'total_discounted_price': total_discounted_price,
        }

        return render(
            request,
            self.template_name,
            context,
        )

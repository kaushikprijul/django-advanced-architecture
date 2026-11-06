from django.http import HttpResponseNotAllowed


class VisitTrackingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("Request Path:", request.path)

        if request.user.is_authenticated:
            print("User:", request.user.username)
        else:
            print("User: Anonymous")

        if request.method not in ['GET', 'POST']:
            return HttpResponseNotAllowed(['GET', 'POST'])

        request.session['visit_count'] = (
            request.session.get('visit_count', 0) + 1
        )

        page_visits = request.session.get('page_visits', {})

        page_visits[request.path] = (
            page_visits.get(request.path, 0) + 1
        )

        request.session['page_visits'] = page_visits

        previous_page = request.session.get('last_visited_page')

        request.session['previous_page'] = previous_page

        request.session['last_visited_page'] = request.path
        print("Visit Count:", request.session['visit_count'])

        response = self.get_response(request)

        print("Response Status:", response.status_code)

        return response
def visit_context(request):

    return {
        'visit_count': request.session.get('visit_count', 0),

        'last_visited_page': request.session.get(
            'last_visited_page', ''
        ),

        'previous_page': request.session.get(
            'previous_page', ''
        ),

        'page_visits': request.session.get(
            'page_visits', {}
        )
    }
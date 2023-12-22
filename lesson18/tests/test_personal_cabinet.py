


def test_go_back_to_dashboard(dashboard):
    personal_page = dashboard.bypass_login()
    personal_page.got_to_main_page2()
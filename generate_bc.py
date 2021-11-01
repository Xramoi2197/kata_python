def generate_bc(url, separator):
    if "http" in url:
        url = url.split("//")[1]
    dirs = url.split("/")[1:]
    if len(dirs) == 0:
        return '<span class="active">HOME</span>'
    main_dir = dirs.pop().split("#")[0].split("?")[0].split(".")[0]
    if main_dir == "index":
        if len(dirs) == 0:
            return '<span class="active">HOME</span>'
        main_dir = dirs.pop()
    elif main_dir == "":
        return '<span class="active">HOME</span>'
    main_dir = f'<span class="active">{acron_dir(main_dir)}</span>'
    url = "/"
    bc_menus = [f'<a href="/">HOME</a>']
    for dir in dirs:
        url += dir + "/"
        bc_menus.append(f'<a href="{url}">{acron_dir(dir)}</a>')
    bc_menus.append(main_dir)
    return separator.join(bc_menus)


def acron_dir(dir):
    ignore_list = [
        "the",
        "of",
        "in",
        "from",
        "by",
        "with",
        "and",
        "or",
        "for",
        "to",
        "at",
        "a",
    ]
    words = dir.split("-")
    if len(dir) > 30:
        result = ""
        for word in words:
            if word not in ignore_list:
                result += word[0]
        return result.upper()
    return " ".join(word.upper() for word in words)


if __name__ == "__main__":
    assert (
        generate_bc("mysite.com/pictures/holidays.html", " : ")
        == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
    )
    assert (
        generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ")
        == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
    )
    assert (
        generate_bc(
            "www.microsoft.com/important/confidential/docs/index.htm#top", " * "
        )
        == '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
    )
    assert (
        generate_bc(
            "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp",
            " > ",
        )
        == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
    )
    assert (
        generate_bc(
            "www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
            " + ",
        )
        == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
    )
    assert (
        generate_bc(
            "www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/",
            " + ",
        )
        == '<span class="active">HOME</span>'
    )
    print(
        generate_bc(
            "https//www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
            " + ",
        )
    )

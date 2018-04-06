---
layout: page
title: Projects
permalink: "/projects/"
---

This section of the site contains overviews of various projects I have worked on.

<div class="posts">
  {% for post in site.categories.research %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <span class="post-date">{{ post.date | date_to_string }}</span>

    {{ post.content }}
  </div>
  {% endfor %}
</div>

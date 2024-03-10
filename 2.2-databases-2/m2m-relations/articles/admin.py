from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']

# @admin.register(ArticleScope)
# class ArticleScopeAdmin(admin.ModelAdmin):
#     list_display = ['tag', 'article', 'scopes']
#     list_filter = ['tag']

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline,]
from modeltranslation.translator import translator, TranslationOptions
from .models import category, subcategory, item, item_terms, item_files, discount, coupon, shop_page, item_photos


class CategoryTranslationOptions(TranslationOptions):
    fields = (
    'is_active', 'keywords', 'description', 'title', 'name', 'figure_size_heading', 'paper_size_heading', 'color_heading', 'difficulty_heading', 'time_heading',
    'paper_amount_heading', 'connected_items_heading', 'bottom_heading', 'delivery_heading', 'other_models_heading', 'index_text')


class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('is_active', 'keywords', 'description', 'title', 'name')


class ItemTranslationOptions(TranslationOptions):
    fields = (
    'is_active', 'keywords', 'description', 'title', 'name', 'video_title', 'figure_size', 'paper_size', 'color', 'difficulty', 'time', 'paper_amount', 'about',
    'bottom_list', 'bottom_link_title', 'bottom_link', 'bottom_text')


class ItemTermsTranslationOptions(TranslationOptions):
    fields = ('text',)


class ItemFilesTranslationOptions(TranslationOptions):
    fields = ('file',)

class ItemPhotosTranslationOptions(TranslationOptions):
    fields = ()


class DiscountTranslationOptions(TranslationOptions):
    fields = ('is_active', 'name', 'type', 'starts', 'ends')


class CouponTranslationOptions(TranslationOptions):
    fields = ('is_active', 'name', 'usage', 'type', 'starts', 'ends')


class ShopPageTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'all', 'no_items', 'increase', 'decrease', 'popular', 'alphabet', 'difficult', 'cart',
              'compare', 'figure_size', 'complexity', 'assembly_time', 'number', 'number_size',
              'another_items', 'to_do', 'megabyte', 'delivery', 'another_models', 'see_more',
              'adding_cart', 'color', 'page_not_found', 'new_start', 'of', 'shop', 'check_order',
              'more', 'less', 'total', 'promo_code')


translator.register(category, CategoryTranslationOptions)
translator.register(subcategory, SubcategoryTranslationOptions)
translator.register(item, ItemTranslationOptions)
translator.register(item_terms, ItemTermsTranslationOptions)
translator.register(item_photos, ItemPhotosTranslationOptions)
translator.register(item_files, ItemFilesTranslationOptions)
translator.register(discount, DiscountTranslationOptions)
translator.register(coupon, CouponTranslationOptions)
translator.register(shop_page, ShopPageTranslationOptions)

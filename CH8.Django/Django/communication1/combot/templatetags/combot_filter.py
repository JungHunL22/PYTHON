from django import template

register=template.Library() # 템플릿 태그를 lib에 등록해서 사용해야 하므로 관련 객체를 생성

@register.filter
def sub(value,arg):
    return value-arg # value에 대응되는 값에서 arg에 대응되는 값을 뺀 결과를 반환

# counter|sub:index
# value  | 필터명:arg
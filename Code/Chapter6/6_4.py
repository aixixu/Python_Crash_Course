programming_term = {
    'function':'严格来说，是指 def 块或 lambda 表达式计算得到的对象。通常，函数这个词用于表示任何可调用的对象，例如方法，有时甚至表示类。官方文档中的内置函数列表列出了几个内置的类，例如dict、range和str。另见可调用的对象词条。',
    'collection':'泛指由元素组成，可以单独访问各个元素的数据结构。有些集合可以包含任意类型的对象（参见容器词条），有些则只能包含一种原子类型的对象（参见平坦序列词条）。list和bytes都是集合，只不过list是容器，而bytes是平坦序列。',
    'type':'程序中的各种数据，限定可取的值和可对数据做的操作。有些Python类型近似于机器数据类型（例如float和bytes），而另一些则是机器数据类型的扩展（例如，int不受CPU字长的限制，str包含多字节Unicode数据码位）和特别高层的抽象（例如dict、 deque，等等）。类型分为两类：用户定义的类型和解释器内置的类型。在Python2.2统一类型和类之前，类型和类是不同的实体，用户定义的类不能扩展内置的类型。而在那之后，内置的类型和新式类兼容了，类是type的实例。在Python 3中，所有类都是新式类。',
    'iterator':'实现了无参数方法__next__的对象；这个方法返回级数里的下一个元素，如果没有元素了就抛出StopIteration异常。在Python中，迭代器还实现了__iter__方法，因此迭代器也是可迭代的对象。根据最初的设计模式，经典迭代器返回集合里的元素。生成器也是迭代器，不过更灵活。',
    'generator':'使用生成器函数或生成器表达式构建的迭代器，无需迭代集合就可能生成值。生成斐波纳契数列的生成器是个典型示例，这是一种无穷数列，在集合中绝对放不下。这个术语除了表示调用生成器函数得到的对象之外，有时还表示生成器函数。',
}
term_ins = ['value','integer','floating point','string','variable']
explantion_ins = ['就是在程序中，我们操作数据的基本单位','又叫做整数类型，用来表达整数的数据类型','用来表示带小数部分的数','用来表示一串字符的类型','引用一个值，这个值的名称']

for i in range(5):
    programming_term[term_ins[i]] = explantion_ins[i]


for pythonterm, explanation in programming_term.items():
    print(f"{pythonterm}:{explanation}.")


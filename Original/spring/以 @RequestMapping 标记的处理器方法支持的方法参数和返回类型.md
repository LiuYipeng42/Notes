## 以 @RequestMapping 标记的处理器方法支持的方法参数和返回类型

### 1. 支持的方法参数类型

1. **HttpServlet 对象**，主要包括HttpServletRequest 、HttpServletResponse 和HttpSession 对象。 这些参数Spring 在调用处理器方法的时候会自动给它们赋值，所以当在处理器方法中需要使用到这些对象的时候，可以直接在方法上给定一个方法参数的申明，然后在方法体里面直接用就可以了。但是有一点需要注意的是在使用HttpSession 对象的时候，如果此时HttpSession 对象还没有建立起来的话就会有问题。

2. Spring 自己的**WebRequest 对象**。 使用该对象可以访问到存放在HttpServletRequest 和HttpSession 中的属性值。

3. **InputStream**、**OutputStream**、**Reader 和Writer**。InputStream 和 Reader 是针对HttpServletRequest 而言的，可以从里面取数据；OutputStream 和 Writer 是针对HttpServletResponse 而言的，可以往里面写数据。

4. 使用**@PathVariable**、**@RequestParam**、**@CookieValue** 和 **@RequestHeader** 标记的参数。

5. 使用 **@ModelAttribute** 标记的参数。

6. **java.util.Map** 、**Spring 封装的Model 和 ModelMap**。 这些都可以用来封装模型数据，用来给视图做展示。

7. **实体类**。可以用来接收上传的参数。

8. **Spring 封装的MultipartFile**。用来接收上传文件的。

9. **Spring 封装的 Errors 和 BindingResult 对象**。这两个对象参数必须紧接在需要验证的实体对象参数之后，它里面包含了实体对象的验证结果。

### 2. 支持的返回类型

1. 一个包含模型和视图的 **ModelAndView 对象**。

2. 一个**模型对象**，这主要包括Spring 封装好的**Model 和 ModelMap**，以及**java.util.Map**，当没有视图返回的时候视图名称将由RequestToViewNameTranslator 来决定。

3. 一个 **View 对象**。这个时候如果在渲染视图的过程中模型的话就可以给处理器方法定义一个模型参数，然后在方法体里面往模型中添加值。

4. 一个**String 字符串**。这往往代表的是一个**视图名称**。这个时候如果需要在渲染视图的过程中需要模型的话就可以给处理器方法一个模型参数，然后在方法体里面往模型中添加值就可以了。

5. 返回值是**void**。这种情况一般是我们直接把返回结果写到 HttpServletResponse 中了，如果没有写的话，那么Spring 将会利用 RequestToViewNameTranslator 来返回一个对应的视图名称。如果视图中需要模型的话，处理方法与返回字符串的情况相同。

6. 如果处理器方法被注解@ResponseBody 标记的话，那么处理器方法的任何返回类型都会通过 HttpMessageConverters 转换之后写到 HttpServletResponse 中，而不会像上面的那些情况一样当做视图或者模型来处理。

7. 除以上几种情况之外的其他任何返回类型都会被当做模型中的一个属性来处理，而返回的视图还是由 RequestToViewNameTranslator 来决定，添加到模型中的属性名称可以在该方法上用 @ModelAttribute(“attributeName”) 来定义，否则将使用返回类型的类名称的首字母小写形式来表示。使用 @ModelAttribute 标记的方法会在@RequestMapping 标记的方法执行之前执行。
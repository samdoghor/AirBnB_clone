# AirBnB Clone - Web static

### Description:
In the realm of web development, the term "Web static" refers to the creation and styling of static web pages using HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets). These static pages do not involve dynamic content generation or server-side processing. Instead, they serve as the visual representation of the web content.

### HTML (HyperText Markup Language)

- **What it is:** HTML is the foundation of web pages. It provides a structured way to define the content of a web page using elements and tags.
- **How to create an HTML page:** You can create an HTML page using a simple text editor (like Notepad) and saving the file with a .html extension. Here's a basic structure:

```
<!DOCTYPE html>
<html>
  <head>
    <title>My Web Page</title>
  </head>

  <body>
    <h1>Welcome to my page!</h1>
    <p>This is some content.</p>
  </body>
</html>
```

### Markup Language
A markup language is a set of codes that adds meaning and structure to plain text. HTML is an example of a markup language. It doesn't define how the content is displayed, but rather what it represents (heading, paragraph, etc.).

### DOM (Document Object Model)
The DOM is a tree-like representation of an HTML document that the browser creates when it loads a web page. It allows you to access and manipulate the content and structure of the page using JavaScript.

### Element/Tag
An element (or tag) is the basic building block of an HTML document. It's defined by opening and closing tags (e.g., <h1> and </h1>). Elements represent specific parts of your content (headings, paragraphs, images, etc.).

### Attribute
An attribute is a way to provide additional information about an element. It's specified within the opening tag (e.g., `<img src="image.jpg" alt="My Image">`). Attributes can define things like image source, element ID, classes, or other properties.

### How the Browser Loads a Webpage
- **Request:** When you enter a URL in the address bar, your browser sends a request to the web server for the specified resource (HTML file).
- **Response:** The server sends the HTML file back to the browser.
Parsing: The browser parses the HTML file, creating the DOM tree.
- **Rendering:** The browser uses the DOM tree to render the content and layout of the page, including fetching and displaying external resources like images and stylesheets.

### CSS (Cascading Style Sheets)
CSS is a language used to style the appearance of an HTML document. It controls things like fonts, colors, layout, positioning, and more.
How to add style to an element: You can add CSS styles to elements using inline styles (directly in the element tag), internal stylesheets (defined within the `<head>` section of the HTML), or external stylesheets (separate .css files linked to the HTML).

### Class
A class is a reusable way to apply styles to multiple elements. You can assign a class name (e.g., .my-class) to elements using the class attribute. Then, in your CSS, you can define styles for elements with that class.

### Selector
A CSS selector is a pattern that specifies which HTML elements a particular style rule should be applied to. Examples include element names (e.g., p), class names (e.g., .my-class), ID selectors (e.g., #unique-id), and more complex combinations.

### Computing CSS Specificity Value
Specificity is a way to determine which CSS rule wins when multiple rules target the same element. It's calculated based on a point system:
- Inline styles: 1000 (highest)
- ID selectors: 100 points each
- Class, pseudo-class, or attribute selectors: 10 points each
- Element type or pseudo-element: 1 point each The rule with the highest specificity value takes precedence.

### Box Model in CSS
The CSS box model is a way to represent an element as a rectangular box with four parts:
- Content: The actual content of the element (text, images, etc.).
- Padding: The space between the content and the border.
- Border: The line around the element's content and padding.
- Margin: The space outside the border of the element. You can use CSS properties like padding, border, and margin to control the dimensions of each part of the box model.
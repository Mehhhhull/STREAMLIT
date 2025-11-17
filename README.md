# Streamlit Learning

Streamlit is a python framework. Uses declarative python code.
NO HTML, CSS, JS required. Pure PYTHON.

## Chapter 1: Basic UI Elements

**Covered:**
- `st.title()` - Main heading
- `st.subheader()` - Subheading
- `st.text()` - Plain text display
- `st.write()` - Universal display function
- `st.selectbox()` - Dropdown selection widget
- `st.success()` - Success message box

**Key Concepts:**
- Interactive widgets automatically trigger reruns
- F-strings for dynamic content display
- Simple syntax for building UI components

## Chapter 2: Interactive Widgets

**Covered:**
- `st.button()` - Clickable button
- `st.checkbox()` - Toggle checkbox
- `st.radio()` - Radio button selection
- `st.selectbox()` - Dropdown menu
- `st.slider()` - Numeric slider with min/max/default
- `st.number_input()` - Number input with step control
- `st.text_input()` - Text input field
- `st.date_input()` - Date picker

**Key Concepts:**
- Conditional rendering with if statements
- Widget state management
- Input validation and constraints
- Multiple input types for different data

## Chapter 3: Layout & Advanced UI

**Covered:**
- `st.columns()` - Multi-column layout
- `st.image()` - Display images from URLs
- `st.sidebar` - Sidebar widgets
- `st.expander()` - Collapsible content sections
- `st.markdown()` - Markdown formatting support

**Key Concepts:**
- Layout control with columns
- Context managers (`with` statement) for scoped content
- Sidebar for persistent controls
- External image loading
- Markdown syntax (headers, blockquotes)

## Chapter 4: Data Handling with Pandas

**Covered:**
- `st.file_uploader()` - File upload widget with type filtering
- `st.dataframe()` - Interactive data table display
- `pd.read_csv()` - Reading CSV files into pandas DataFrame
- `df.describe()` - Statistical summary of data
- `df["column"].unique()` - Getting unique values from column
- DataFrame filtering with boolean indexing

**Key Concepts:**
- File upload and validation
- Integration with pandas for data manipulation
- Conditional data display based on file upload
- Dynamic filtering with selectbox
- Statistical analysis display
- Working with CSV data in Streamlit

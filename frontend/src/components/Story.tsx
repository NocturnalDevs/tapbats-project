import { useState, useEffect } from 'react'; // Import React hooks

const Story = () => {
  // State to track the current page number
  const [pageNumber, setPageNumber] = useState(1); // Default: Page 1
  // State to track the last page number (total number of pages)
  const [lastPage, setLastPage] = useState(1); // Start with 1, will be updated with the total number of pages
  // State to store the URL of the current page's image
  const [imageUrl, setImageUrl] = useState<string | null>(null); // Default: No image
  // State to track if the input value exceeds the last page
  const [inputError, setInputError] = useState<string | null>(null); // Default: No error
  // State to track the raw input value (allows the input field to be empty temporarily)
  const [inputValue, setInputValue] = useState<string>(pageNumber.toString()); // Default: Current page number as a string

  /**
   * Simulates fetching data from a database.
   * Replace this with an actual API call in production.
   */
  useEffect(() => {
    const fetchPageData = () => {
      // Simulate fetching total page count (e.g., number of images in the database)
      setTimeout(() => {
        // Example: Simulate getting total pages from the database
        const totalPages = 10; // Replace this with the actual number of images from the database
        setLastPage(totalPages); // Update the last page number

        // Simulate fetching the image URL for the current page
        const fetchedImageUrl = `https://example.com/images/story-page-${pageNumber}.jpg`; // Example URL, change as per your database
        setImageUrl(fetchedImageUrl); // Set the fetched image URL
      }, 500); // Simulate 500ms delay for fetching data
    };

    fetchPageData(); // Fetch data when the page number changes
  }, [pageNumber]); // Dependency array to fetch data whenever pageNumber changes

  /**
   * Handles button clicks for navigation (First, Prev, Next, Last).
   * @param action - The action to perform (e.g., 'first', 'prev', 'next', 'last').
   */
  const handleClick = (action: string) => {
    switch (action) {
      case 'first':
        setPageNumber(1); // Set the page to the first page
        break;
      case 'prev':
        setPageNumber((current) => Math.max(1, current - 1)); // Go to the previous page
        break;
      case 'next':
        setPageNumber((current) => Math.min(lastPage, current + 1)); // Go to the next page
        break;
      case 'last':
        setPageNumber(lastPage); // Set the page to the last page
        break;
      default:
        break; // Do nothing for unknown actions
    }
    setInputError(null); // Clear any input error when navigating
  };

  /**
   * Handles changes in the page number input field.
   * @param event - The change event from the input field.
   */
  const handlePageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value; // Get the raw input value as a string
    setInputValue(value); // Update the input value state

    // If the input is empty, do nothing (allow the field to be empty temporarily)
    if (value === '') {
      setInputError(null); // Clear any error message
      return;
    }

    // Parse the input value as an integer
    const parsedValue = parseInt(value, 10);
    if (!isNaN(parsedValue)) {
      if (parsedValue > lastPage) {
        setInputError(`The maximum page number is ${lastPage}.`); // Set error message
      } else {
        setPageNumber(parsedValue); // Update the page number if the value is valid
        setInputError(null); // Clear the error message
      }
    }
  };

  // Update the input value when the page number changes (e.g., via navigation buttons)
  useEffect(() => {
    setInputValue(pageNumber.toString());
  }, [pageNumber]);

  return (
    <div className="flex flex-col flex-grow">
      {/* Main content area displaying the image */}
      <div className="bg-[#121116] text-gray-200 | flex-grow p-4 | eclipse-themed-border">
        {/* Display the image for the current page if it exists */}
        {imageUrl && (
          <div className="mt-4">
            <img
              src={imageUrl}
              alt={`Page ${pageNumber}`}
              className="w-full h-auto rounded-md"
            />
          </div>
        )}
        {/* Coming Soon Message */}
        <div className="mt-4 text-center text-2xl text-gray-500 font-semibold">
          Coming Soon!
        </div>
      </div>

      {/* Controls Section for navigating the story */}
      <div className="text-gray-200 font-bold | flex items-center justify-between space-x-1 | pt-2 pb-2 -mb-2">
        {/* First Button */}
        <button
          className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
          onClick={() => handleClick('first')} // Handle First button click
        >
          First
        </button>

        {/* Previous Button */}
        <button
          className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
          onClick={() => handleClick('prev')} // Handle Prev button click
        >
          Prev
        </button>

        {/* Page Number Input */}
        <input
          type="number"
          value={inputValue} // Use the raw input value
          onChange={handlePageChange}
          className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
        />

        {/* Next Button */}
        <button
          className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
          onClick={() => handleClick('next')} // Handle Next button click
        >
          Next
        </button>

        {/* Last Button */}
        <button
          className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
          onClick={() => handleClick('last')} // Handle Last button click
        >
          Last
        </button>
      </div>

      {/* Display error message if the input value exceeds the last page */}
      {inputError && (
        <div className="text-red-500 text-center mt-2">
          {inputError}
        </div>
      )}
    </div>
  );
};

export default Story;
import { useState } from 'react';
import PaginationControls from '../components/PaginationControls';

function Story() {
    const [pageNumber, setPageNumber] = useState(1);
    const [inputError, setInputError] = useState<string | null>(null);
    const [inputValue, setInputValue] = useState<string>(pageNumber.toString());
    const [imageLoading, setImageLoading] = useState(true);

    // Placeholder data for story pages
    const unlockedStoryPages = [
        // { pageNumber: 1, pageImage: 'https://via.placeholder.com/600x800' },
    ];

    const lastPage = unlockedStoryPages.length;

    const handleClick = (action: string): void => {
        switch (action) {
            case 'first':
                setPageNumber(1);
                break;
            case 'prev':
                setPageNumber((current) => Math.max(1, current - 1));
                break;
            case 'next':
                setPageNumber((current) => Math.min(lastPage, current + 1));
                break;
            case 'last':
                setPageNumber(lastPage);
                break;
            default:
                break;
        }
        setInputError(null);
    };

    const handlePageChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
        const value = event.target.value;
        setInputValue(value);

        if (value === '') {
            setInputError(null);
            return;
        }

        const parsedValue = parseInt(value, 10);
        if (!isNaN(parsedValue)) {
            if (parsedValue > lastPage) {
                setInputError(`The maximum page number is ${lastPage}.`);
            } else {
                setPageNumber(parsedValue);
                setInputError(null);
            }
        }
    };

    const currentPage = unlockedStoryPages.find((page) => page.pageNumber === pageNumber);
    const imageUrl = currentPage ? currentPage.pageImage : null;

    return (
        <div className="flex flex-col flex-grow overlow-auto">
            {/* Top Pagination Controls */}
            <PaginationControls
                position="top"
                pageNumber={pageNumber}
                lastPage={lastPage}
                onPageChange={handleClick}
                inputValue={inputValue}
                onInputChange={handlePageChange}
                inputError={inputError}
            />

            {/* Story Content */}
            <div className="bg-[#121116] text-gray-200 | flex-grow p-2 | eclipse-themed-border">
                <div className="text-center text-2xl text-gray-500 font-semibold">
                    {`Page ${pageNumber}`}
                </div>
                {imageUrl ? (
                    <div className="mt-2 rounded-md">
                        {imageLoading && (
                            <div className="flex items-center justify-center h-64">
                                <div className="text-gray-500">Loading image...</div>
                            </div>
                        )}
                        <img
                            src={imageUrl}
                            alt={`Page ${pageNumber}`}
                            className="w-full h-fit"
                            onLoad={() => setImageLoading(false)}
                            style={{ display: imageLoading ? 'none' : 'block' }}
                        />
                    </div>
                ) : (
                    <div className="mt-2 rounded-md bg-gray-700 flex items-center justify-center h-64">
                        <div className="text-gray-500">Error loading image.</div>
                    </div>
                )}
            </div>

            {/* Bottom Pagination Controls */}
            <PaginationControls
                position="bottom"
                pageNumber={pageNumber}
                lastPage={lastPage}
                onPageChange={handleClick}
                inputValue={inputValue}
                onInputChange={handlePageChange}
                inputError={inputError}
            />
        </div>
    );
}

export default Story;
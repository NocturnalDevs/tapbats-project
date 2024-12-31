import { useState, useEffect } from 'react';
import { useStoryContext } from '../context/StoryContext';
import PaginationControls from '../components/PaginationControls';

function Story() {
    const { allStoryPages, areAssetsLoaded } = useStoryContext();
    const [pageNumber, setPageNumber] = useState(1);
    const [inputError, setInputError] = useState<string | null>(null);
    const [inputValue, setInputValue] = useState<string>(pageNumber.toString());

    const lastPage = allStoryPages.length;

    // Synchronize inputValue with pageNumber
    useEffect(() => {
        setInputValue(pageNumber.toString());
    }, [pageNumber]);

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
            }
            else {
                setPageNumber(parsedValue);
                setInputError(null);
            }
        }
    };

    const currentPage = allStoryPages.find((page) => page.pageNumber === pageNumber);
    const imageUrl = currentPage ? currentPage.pageImage : null;

    // Show a placeholder while assets are loading
    if (!areAssetsLoaded) {
        return (
            <div className="flex flex-col flex-grow items-center justify-center">
                <div className="text-gray-500 text-xl font-bold">Loading story...</div>
            </div>
        );
    }

    return (
        <div>
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
                {imageUrl && (
                    <div className="mt-2 rounded-md">
                        <img
                            src={imageUrl}
                            alt={`Page ${pageNumber}`}
                            className="w-full h-fit"
                        />
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
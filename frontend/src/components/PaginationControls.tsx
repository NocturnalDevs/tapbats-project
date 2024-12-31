import React from 'react';

type PaginationControlsProps = {
    position: 'top' | 'bottom'; // Restrict position to 'top' or 'bottom'
    pageNumber: number;
    lastPage: number;
    onPageChange: (action: string) => void;
    inputValue: string;
    onInputChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    inputError: string | null;
};

const PaginationControls = ({
    position,
    pageNumber,
    lastPage,
    onPageChange,
    inputValue,
    onInputChange,
    inputError,
}: PaginationControlsProps) => {
    return (
        <>
            {/* Render error message at the top if position is 'bottom' */}
            {position === 'bottom' && inputError && (
                <div className="text-red-500 text-center mt-2">
                    {inputError}
                </div>
            )}

            {/* Pagination controls */}
            <div
                className={`text-gray-200 font-bold | flex items-center justify-between space-x-1 ${
                    position === 'top' ? 'pb-2' : 'pt-2'
                }`}
            >
                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => onPageChange('first')}
                >
                    First
                </button>

                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => onPageChange('prev')}
                >
                    Prev
                </button>

                <input
                    type="number"
                    value={inputValue}
                    onChange={onInputChange}
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                />

                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => onPageChange('next')}
                >
                    Next
                </button>

                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => onPageChange('last')}
                >
                    Last
                </button>
            </div>

            {/* Render error message at the top if position is 'bottom' */}
            {position === 'top' && inputError && (
                <div className="text-red-500 text-center mb-2">
                    {inputError}
                </div>
            )}
        </>
    );
};

export default PaginationControls;
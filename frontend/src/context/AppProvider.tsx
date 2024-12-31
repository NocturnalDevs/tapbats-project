import { UserProvider } from './UserContext';
import { GemProvider } from './GemContext';
import { QuestProvider } from './QuestContext';
import { StoryProvider } from './StoryContext';
import { ReferralProvider } from './ReferralContext';

type AppProviderProps = {
    children: React.ReactNode;
};

export const AppProvider = ({ children }: AppProviderProps) => {
    return (
        <UserProvider>
            <GemProvider>
                <QuestProvider>
                    <StoryProvider>
                        <ReferralProvider>
                            {children}
                        </ReferralProvider>
                    </StoryProvider>
                </QuestProvider>
            </GemProvider>
        </UserProvider>
    );
};
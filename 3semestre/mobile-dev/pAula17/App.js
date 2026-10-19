import { SafeAreaProvider } from "react-native-safe-area-context";
import RootDrawer from "./src/routes/RootDrawer";
import { NavigationContainer } from "@react-navigation/native";

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <RootDrawer />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}

import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import CarListScreen from "./screens/CarListScreen";
import CreateCarScreen from "./screens/AddCarScreen";
import CarDetailsScreen from "./screens/CarDetailsScreen";
import StaffScreen from "./screens/StaffScreen";
import OrdersScreen from "./screens/OrdersScreen";
// import InProgressEventScreen from "./screens/InProgressEventScreen";
// import AnalyticsScreen from "./screens/AnalyticsScreen";

const Stack = createStackNavigator();

const App = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="CarList" component={CarListScreen}/>
                <Stack.Screen name="CreateCar" component={CreateCarScreen}/>
                <Stack.Screen name="CarDetails" component={CarDetailsScreen}/>
                <Stack.Screen name="StaffSection" component={StaffScreen}/>
                <Stack.Screen name="SupplierSection" component={OrdersScreen}/>
                {/*<Stack.Screen name="InProgressEvent" component={InProgressEventScreen}/>*/}
                {/*<Stack.Screen name="Analytics" component={AnalyticsScreen}/>*/}
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default App;
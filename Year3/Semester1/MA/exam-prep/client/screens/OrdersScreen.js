import React, {useEffect, useState} from 'react';
import {View, Text, FlatList, StyleSheet, ActivityIndicator, TouchableOpacity} from 'react-native';
import axios from 'axios';
import {useNavigation} from "@react-navigation/native";
import Toast from "react-native-toast-message";
import {appendLog} from "../log/Logger";


const OrdersScreen = () => {
    const navigation = useNavigation();
    const [cars, setCars] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [isEmpty, setIsEmpty] = useState(false);

    useEffect(() => {
        loadCars();
    }, []);

    const loadCars = async () => {
        setIsLoading(true);
        try {
            const response = await axios.get('http://192.168.1.134:2406/carorders');

            setCars(response.data);
            if(response.data.length === 0)
                setIsEmpty(true);
            appendLog('Fetched car orders successfully');
        } catch (error) {
            appendLog('Error fetching car orders');
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        if (isEmpty) {
            Toast.show({
                type: 'success',
                text1: 'No pending orders',
                visibilityTime: 5000,
            });
        }
    }, [isEmpty]);


    return (
        <View style={styles.container}>
            {isLoading ? (
                <ActivityIndicator size="large" color="#0000ff"/>
            ) : (
                <FlatList
                    data={cars}
                    keyExtractor={(item) => item.id.toString()}
                    showsVerticalScrollIndicator={false}
                    renderItem={({item}) => (
                        <View style={styles.eventItem}>
                            <Text style={styles.title}>{item.id}</Text>
                            <Text>Supplier: {item.supplier}</Text>
                            <Text>Details: {item.details}</Text>
                            <Text>Status: {item.status}</Text>
                            <Text>Quantity: {item.quantity}</Text>
                            <Text>Type: {item.type}</Text>
                        </View>
                    )}
                />
            )}
            <Toast/>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f2f2f2',
        padding: 10,
    },
    eventItem: {
        backgroundColor: '#fff',
        padding: 10,
        marginVertical: 8,
        borderRadius: 5,
    },
    title: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    enrollButton: {
        backgroundColor: '#007AFF',
        padding: 10,
        borderRadius: 5,
        marginTop: 10,
    },
    enrollButtonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
        textAlign: 'center',
    }
});

export default OrdersScreen;